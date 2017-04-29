package com.example.as.origins.fragments;

import android.content.Context;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseExpandableListAdapter;
import android.widget.ExpandableListView;
import android.widget.SimpleExpandableListAdapter;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import com.example.as.origins.R;


public class TrailsFragment extends Fragment {

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_trails, null);
        ExpandableListView elv = (ExpandableListView) v.findViewById(R.id.trails_list);
        elv.setAdapter(new SavedTabsListAdapter());
        return v;
    }

    public class SavedTabsListAdapter extends BaseExpandableListAdapter {

        private String[] groups = { "Маршрут 1", "Маршрут 2", "Маршрут 3", "Маршрут 4", "Маршрут 5" };

        private String[][] children = {
                { "Очень интересный маршрут" },
                { "Этот маршрут подходит для молодых людей" },
                { "Можете ходить? Пройдите этот маршрут!" },
                { "Будьте осторожны, проходя этот маршрут" },
                { "Говорят, этот маршрут еще никому не удавалось пройти до конца" }
        };

        @Override
        public int getGroupCount() {
            return groups.length;
        }

        @Override
        public int getChildrenCount(int i) {
            return children[i].length;
        }

        @Override
        public Object getGroup(int i) {
            return groups[i];
        }

        @Override
        public Object getChild(int i, int i1) {
            return children[i][i1];
        }

        @Override
        public long getGroupId(int i) {
            return i;
        }

        @Override
        public long getChildId(int i, int i1) {
            return i1;
        }

        @Override
        public boolean hasStableIds() {
            return true;
        }

        @Override
        public View getGroupView(int i, boolean b, View view, ViewGroup viewGroup) {
            TextView textView = new TextView(TrailsFragment.this.getActivity());
            textView.setText(getGroup(i).toString());
            return textView;
        }

        @Override
        public View getChildView(int i, int i1, boolean b, View view, ViewGroup viewGroup) {
            TextView textView = new TextView(TrailsFragment.this.getActivity());
            textView.setText(getChild(i, i1).toString());
            return textView;
        }

        @Override
        public boolean isChildSelectable(int i, int i1) {
            return true;
        }

    }


}
